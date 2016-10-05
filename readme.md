#SUTD 50.002 Group Projects

###Members:

- 1001526 Eric Teo
- 1001694 Tasya Aditya Rukmana
- 1001692 Nguyen The Hung (Stanley)

###MOJO Adder tester:

- Uses I/O shield.
- Displays the test results in the rightmost leds.
- Displays the input to adder in the middle leds. (In order from right to left, abc.)
- Displays the expected output from adder in the first 2 left leds (first from right.)
- Displays actual output from adder in the last 2 left leds.
- The step module runs on its own reset. The state machine will reset the step module when initialised to make sure the step module is in sync.
Advances to next test after 2s.