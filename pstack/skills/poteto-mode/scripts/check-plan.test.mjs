import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const checker = fileURLToPath(new URL("./check-plan.mjs", import.meta.url));
const rule = "Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.";

function plan(model = "grok-4.6-fast-xhigh", readInstructions = "git show origin/main:pstack/skills/swarm/SKILL.md") {
	return `# Ship the change

## How to read this

One box is one unit of work and names the evidence. Check a box only when its evidence exists.
Run playbooks/autopilot-full.md.
${rule}

## Program checklist

### Arm the program

- [ ] Arm /goal for this change.
- [ ] ${readInstructions}
- [ ] Run a 30-minute audit and send a status message.

### Spawn owners

- [ ] Assign one owner.

### PR mechanics

- [ ] Open the PR.

### Verdict and merge

- [ ] Obtain an independent verdict.

### Boot recipe

- [ ] Start the app at the PR head.

## Implement the change

**Depends on.** None.

**Files.**

- [ ] Edit app.ts.

**Build.**

- [ ] Implement the behaviour.

**You see.**

- [ ] The app displays the result.

**Verify, unit.** ${rule}

- [ ] Run the focused unit test.

**Verify, live.** ${rule} Ten lanes on \`${model}\` at the PR head.

${Array.from({ length: 10 }, (_, index) => `- [ ] Lane ${index + 1}. Exercise the app. Save \`/tmp/lane-${index + 1}.png\`. Pass when the result appears.`).join("\n")}

**Verify, perf.** ${rule}

- [ ] Metric. Response time.
- [ ] Probe. Repeat the same action.
- [ ] Baseline. Measure trunk first.
- [ ] Rule. Response takes under one second.

**Review gate.** None. This change has no interaction to review.

**Merge.**

- [ ] Merge after verification.

## Close the program

- [ ] Report the outcome.

## Appendix A. Prototype evidence

The existing pattern supplies the implementation.
`;
}

function check(contents) {
	const directory = mkdtempSync(join(tmpdir(), "check-plan-test-"));
	try {
		const path = join(directory, "plan.md");
		writeFileSync(path, contents);
		return spawnSync(process.execPath, [checker, path], { encoding: "utf8" });
	} finally {
		rmSync(directory, { recursive: true, force: true });
	}
}

test("accepts the existing Cursor plan format", () => {
	const result = check(plan());
	assert.equal(result.status, 0, result.stderr);
	assert.match(result.stdout, /1 PR sections, 0 problems/);
});

test("accepts a Codex model and installed plugin instruction reads", () => {
	const result = check(plan("gpt-5.6-sol", "Read installed plugin files from the resolved pstack root at every tick."));
	assert.equal(result.status, 0, result.stderr);
});

test("rejects a plan without an instruction read marker", () => {
	const result = check(plan("gpt-5.6-sol", "Read the application source."));
	assert.equal(result.status, 1);
	assert.match(result.stderr, /Program checklist lacks/);
});

test("rejects a plan missing the tenth live lane", () => {
	const result = check(plan().replace(/^- \[ \] Lane 10\..*\n/m, ""));
	assert.equal(result.status, 1);
	assert.match(result.stderr, /expected 1 to 10/);
});

test("rejects a plan without a named live lane model", () => {
	const result = check(plan(""));
	assert.equal(result.status, 1);
	assert.match(result.stderr, /Verify, live lacks/);
});

for (const goal of ["$goal", "$pstack:goal", "/pstack:goal"]) {
	test(`accepts the native goal reference ${goal}`, () => {
		const result = check(plan().replace("/goal", goal));
		assert.equal(result.status, 0, result.stderr);
	});
}
