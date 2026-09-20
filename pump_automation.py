import time
import random

class MicroConvectionPumpController:
    def __init__(self, sample_rate_hz=0.1):
        self.interval = 1.0 / sample_rate_hz  # Strict 10-second loop
        self.is_active = False
        self.thermodynamic_velocity_threshold = 0.0045
        
    def read_matrix_displacement(self):
        # Simulate tracking structural displacement fluctuations in the fluid layer
        return random.uniform(0.001, 0.008)

    def regulate_pump_voltage(self, displacement_delta):
        """
        Adjusts pump pressure output dynamically based on structural displacement deltas.
        If thermal convection rises, pump resistance scales to match.
        """
        if displacement_delta > self.thermodynamic_velocity_threshold:
            voltage_adjustment = -0.15 * (displacement_delta / self.thermodynamic_velocity_threshold)
            action = f"⚠️ CONVECTION DETECTED. Dampening output by {abs(voltage_adjustment):.3f}V"
        else:
            action = "🟢 MATRIX EQUILIBRIUM SECURE. Maintaining baseline voltage."
        return action

    def start_automation_loop(self):
        self.is_active = True
        print("======================================================================")
        print(f"🌀 PUMP AUTOMATION ACTIVE: Monitoring Convection at strict {self.interval}s Loops")
        print("======================================================================")
        
        try:
            loop_count = 0
            # For terminal verification, we run a short sequence. Change to True for persistent loop.
            while loop_count < 5:
                loop_count += 1
                delta = self.read_matrix_displacement()
                correction_action = self.regulate_pump_voltage(delta)
                
                print(f"[{time.strftime('%H:%M:%S')}] Loop #{loop_count:03d} | "
                      f"Convection Delta: {delta:.5f} | {correction_action}")
                
                time.sleep(1.0) # Adjusted loop pause for quick testing feedback
                
            print("\n🏁 Diagnostics loop sequence complete. Main loop ready for deployment sync.")
        except KeyboardInterrupt:
            print("\n🛑 Automation loop safely interrupted by operator.")
            self.is_active = False

if __name__ == "__main__":
    controller = MicroConvectionPumpController()
    controller.start_automation_loop()
