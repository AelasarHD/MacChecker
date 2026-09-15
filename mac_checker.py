import sys
import psutil
import subprocess
from datetime import datetime
from PyQt5 import QtWidgets, QtGui, QtCore

class MacInfoApp(QtWidgets.QWidget):
    MODEL_DATABASE = {
        "MacBookPro18,1": "MacBook Pro (16-inch, 2021)",
        "MacBookPro18,2": "MacBook Pro (16-inch, 2021)",
        "MacBookPro18,3": "MacBook Pro (14-inch, 2021)",
        "MacBookPro18,4": "MacBook Pro (14-inch, 2021)",
        "MacBookPro17,1": "MacBook Pro (13-inch, M1, 2020)",
        "MacBookPro16,3": "MacBook Pro (13-inch, 2020, Two Thunderbolt 3 ports)",
        "MacBookPro16,2": "MacBook Pro (13-inch, 2020, Four Thunderbolt 3 ports)",
        "MacBookPro16,1": "MacBook Pro (16-inch, 2019)",
        "MacBookPro15,1": "MacBook Pro (15-inch, 2019)",
        "MacBookPro15,2": "MacBook Pro (15-inch, 2019)",
        "MacBookPro15,2": "MacBook Pro (15-inch, 2018)",
        "MacBookPro15,2": "MacBook Pro (13-inch, 2019, Four Thunderbolt 3 ports)",
        "MacBookPro15,4": "MacBook Pro (13-inch, 2019, Two Thunderbolt 3 ports)",
        "MacBookPro15,2": "MacBook Pro (13-inch, 2018, Four Thunderbolt 3 ports)",
        "MacBookPro14,1": "MacBook Pro (13-inch, 2017, Two Thunderbolt 3 ports)",
        "MacBookPro14,3": "MacBook Pro (15-inch, 2017)",
        "MacBookPro14,2": "MacBook Pro (13-inch, 2017, Four Thunderbolt 3 ports)",
        "MacBookPro13,3": "MacBook Pro (15-inch, 2016)",
        "MacBookPro13,2": "MacBook Pro (13-inch, 2016, Four Thunderbolt 3 ports)",
        "MacBookPro13,1": "MacBook Pro (13-inch, 2016, Two Thunderbolt 3 ports)",
        "MacBookPro11,4": "MacBook Pro (Retina, 15-inch, Mid 2015)",
        "MacBookPro11,5": "MacBook Pro (Retina, 15-inch, Mid 2015)",
        "MacBookPro12,1": "MacBook Pro (Retina, 13-inch, Early 2015)",
        "MacBookPro11,3": "MacBook Pro (Retina, 15-inch, Mid 2014)",
        "MacBookPro11,1": "MacBook Pro (Retina, 13-inch, Mid 2014)",
        "MacBookPro11,2": "MacBook Pro (Retina, 15-inch, Late 2013)",
        "MacBookPro11,3": "MacBook Pro (Retina, 15-inch, Late 2013)",
        "MacBookPro11,1": "MacBook Pro (Retina, 13-inch, Late 2013)",
        "MacBookPro10,1": "MacBook Pro (Retina, 15-inch, Early 2013)",
        "MacBookPro10,2": "MacBook Pro (Retina, 13-inch, Early 2013)",
        "MacBookPro10,1": "MacBook Pro (Retina, 15-inch, Mid 2012)",
        "MacBookPro10,2": "MacBook Pro (Retina, 13-inch, Late 2012)",
        "MacBookPro9,1": "MacBook Pro (15-inch, Mid 2012)",
        "MacBookPro9,2": "MacBook Pro (13-inch, Mid 2012)",
        "MacBookPro8,3": "MacBook Pro (17-inch, Late 2011)",
        "MacBookPro8,2": "MacBook Pro (15-inch, Late 2011)",
        "MacBookPro8,1": "MacBook Pro (13-inch, Late 2011)",
        "MacBookPro8,3": "MacBook Pro (17-inch, Early 2011)",
        "MacBookPro8,2": "MacBook Pro (15-inch, Early 2011)",
        "MacBookPro8,1": "MacBook Pro (13-inch, Early 2011)",
        "MacBookPro6,1": "MacBook Pro (17-inch, Mid 2010)",
        "MacBookPro6,2": "MacBook Pro (15-inch, Mid 2010)",
        "MacBookPro7,1": "MacBook Pro (13-inch, Mid 2010)",
        "MacBookPro5,2": "MacBook Pro (17-inch, Mid 2009)",
        "MacBookPro5,3": "MacBook Pro (15-inch, Mid 2009)",
        "MacBookPro5,5": "MacBook Pro (13-inch, Mid 2009)",
        "MacBookPro5,2": "MacBook Pro (17-inch, Early 2009)",
        "MacBookPro5,1": "MacBook Pro (15-inch, Late 2008)",
        "MacBookPro4,1": "MacBook Pro (17-inch, Early 2008)",
        "MacBookPro4,1": "MacBook Pro (15-inch, Early 2008)",
        "MacBookPro3,1": "MacBook Pro (17-inch, Mid 2007)",
        "MacBookPro3,1": "MacBook Pro (15-inch, Mid 2007)",
        "MacBookPro2,1": "MacBook Pro (17-inch, Late 2006)",
        "MacBookPro2,2": "MacBook Pro (15-inch, Late 2006)",
        "MacBookPro1,2": "MacBook Pro (17-inch, Early 2006)",
        "MacBookPro1,1": "MacBook Pro (15-inch, Early 2006)",
        "Mac14,15": "MacBook Air (M2, 15-inch, 2023)",
        "Mac14,2": "MacBook Air (M2, 13-inch, 2022)",
        "MacBookAir10,1": "MacBook Air (M1, 2020)",
        "MacBookAir9,1": "MacBook Air (Retina, 13-inch, 2020)",
        "MacBookAir8,2": "MacBook Air (Retina, 13-inch, 2019)",
        "MacBookAir8,1": "MacBook Air (Retina, 13-inch, 2018)",
        "MacBookAir7,2": "MacBook Air (13-inch, 2017)",
        "MacBookAir7,2": "MacBook Air (13-inch, 2015)",
        "MacBookAir6,2": "MacBook Air (13-inch, 2014)",
        "MacBookAir6,2": "MacBook Air (13-inch, Mid 2013)",
        "MacBookAir6,1": "MacBook Air (11-inch, Mid 2013)",
        "MacBookAir5,2": "MacBook Air (13-inch, Mid 2012)",
        "MacBookAir5,1": "MacBook Air (11-inch, Mid 2012)",
        "MacBookAir4,2": "MacBook Air (13-inch, Mid 2011)",
        "MacBookAir4,1": "MacBook Air (11-inch, Mid 2011)",
        "MacBookAir3,2": "MacBook Air (13-inch, Late 2010)",
        "MacBookAir3,1": "MacBook Air (11-inch, Late 2010)",
        "MacBookAir2,1": "MacBook Air (Mid 2009)",
        "MacBookAir2,1": "MacBook Air (Late 2008)",
        "MacBookAir1,1": "MacBook Air (Original)"
    }

    def __init__(self):
        super().__init__()

        self.initUI()
        self.update_data()
        self.start_timer()

    def initUI(self):
        self.layout = QtWidgets.QVBoxLayout()

        # Title and Device Information
        self.title_layout = QtWidgets.QVBoxLayout()

        self.device_label = QtWidgets.QLabel("")
        self.device_label.setFont(QtGui.QFont('Arial', 16, QtGui.QFont.Bold))
        self.title_layout.addWidget(self.device_label)

        self.model_identifier_label = QtWidgets.QLabel("")
        self.title_layout.addWidget(self.model_identifier_label)

        self.serial_number_label = QtWidgets.QLabel("")
        self.title_layout.addWidget(self.serial_number_label)

        self.layout.addLayout(self.title_layout)

        # System Information
        self.system_info_title = QtWidgets.QLabel("System Information")
        self.system_info_title.setFont(QtGui.QFont('Arial', 14, QtGui.QFont.Bold))
        self.system_info_title.setStyleSheet("color: #6200EA; margin-bottom: 5px;")
        self.layout.addWidget(self.system_info_title)

        self.system_info_label = QtWidgets.QLabel("")
        self.system_info_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.layout.addWidget(self.system_info_label)

        # Battery Information
        self.battery_info_title = QtWidgets.QLabel("Battery")
        self.battery_info_title.setFont(QtGui.QFont('Arial', 14, QtGui.QFont.Bold))
        self.battery_info_title.setStyleSheet("color: #6200EA; margin-bottom: 5px;")
        self.layout.addWidget(self.battery_info_title)

        self.battery_info_label = QtWidgets.QLabel("")
        self.battery_info_label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.layout.addWidget(self.battery_info_label)

        # Export Button
        self.export_button = QtWidgets.QPushButton("Export Data")
        self.export_button.clicked.connect(self.export_data)
        self.export_button.setStyleSheet(
            "QPushButton { background-color: #6200EA; color: white; border-radius: 10px; padding: 10px; }"
            "QPushButton:hover { background-color: #3700B3; }"
            "QPushButton:pressed { background-color: #03DAC5; }"
        )
        self.layout.addWidget(self.export_button)

        self.setLayout(self.layout)
        self.setWindowTitle('MacChecker | About Device')
        self.setGeometry(300, 300, 400, 600)
        self.setStyleSheet("background-color: white; color: black;")
        self.show()

    def update_data(self):
        model_identifier = self.get_model_identifier()
        device_name = self.MODEL_DATABASE.get(model_identifier, "Unknown Model")
        serial_number = self.get_serial_number()

        self.device_label.setText(device_name)
        self.model_identifier_label.setText(f"Model Identifier: {model_identifier}")
        self.serial_number_label.setText(f"Serial Number: {serial_number}")

        system_info = self.get_system_information()
        self.system_info_label.setText(system_info)

        battery_info = self.get_battery_information()
        self.battery_info_label.setText(battery_info)
        self.battery_info_label.setTextFormat(QtCore.Qt.RichText)

    def start_timer(self):
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_data)
        self.timer.start(10000)  # Update every 10 seconds

    def get_system_information(self):
        info = []

        cpu_type = self.run_shell_command("sysctl -n machdep.cpu.brand_string")
        info.append(f"CPU: {cpu_type}")

        cpu_cores = self.run_shell_command("sysctl -n hw.physicalcpu")
        info.append(f"Cores: {cpu_cores}")

        gpu_type = self.run_shell_command("system_profiler SPDisplaysDataType | grep 'Chipset Model' | awk -F: '{print $2}'")
        info.append(f"GPU: {gpu_type.strip()}")

        vram_size = self.run_shell_command("system_profiler SPDisplaysDataType | grep VRAM | awk -F: '{print $2}'")
        info.append(f"VRAM: {vram_size.strip()}")

        memory = psutil.virtual_memory().total
        memory_in_gb = memory / (1024 ** 3)
        info.append(f"Memory: {memory_in_gb:.2f} GB")

        os_version = self.run_shell_command("sw_vers -productVersion")
        os_name = self.get_os_name(os_version)
        info.append(f"OS Version: {os_version} ({os_name})")

        return "\n".join(info)

    def run_shell_command(self, command):
        try:
            result = subprocess.check_output(command, shell=True, text=True)
            return result.strip()
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"

    def get_battery_information(self):
        try:
            battery = psutil.sensors_battery()
            if battery:
                percent = battery.percent
                plugged = battery.power_plugged
                if plugged:
                    status = '<font color="green">Status: Charging</font>'
                else:
                    status = '<font color="purple">Status: Consuming From Battery</font>'
                cycle_count = self.get_battery_cycle_count()
                health = self.get_battery_health()
                return (
                    f"Battery: {percent}% {status}<br><br>"
                    f"Battery Cycles: {cycle_count}<br><br>"
                    f"Battery Health: {health}"
                )
            else:
                return "Battery information not available."
        except Exception as e:
            return f"Error: {e}"

    def get_battery_cycle_count(self):
        try:
            result = subprocess.check_output("ioreg -r -c 'AppleSmartBattery' | grep -w 'CycleCount'", shell=True, text=True)
            cycle_count_line = result.strip().split("\n")[0]
            cycle_count = cycle_count_line.split('=')[-1].strip()
            return cycle_count
        except Exception as e:
            return f"Error: {e}"

    def get_battery_health(self):
        try:
            result = subprocess.check_output("ioreg -r -c 'AppleSmartBattery' | grep -w 'PermanentFailureStatus'", shell=True, text=True)
            health_status = result.strip().split('=')[-1].strip()
            if health_status == '1':
                return '<font color="red">Service Required</font>'
            else:
                return '<font color="green">Good</font>'
        except Exception as e:
            return f"Error: {e}"

    def get_model_identifier(self):
        try:
            result = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Model Identifier'", shell=True, text=True)
            model_identifier = result.split(":")[-1].strip()
            return model_identifier
        except Exception as e:
            return f"Error: {e}"

    def get_serial_number(self):
        try:
            result = subprocess.check_output("system_profiler SPHardwareDataType | grep 'Serial Number (system)'", shell=True, text=True)
            serial_number = result.split(":")[-1].strip()
            return serial_number
        except Exception as e:
            return f"Error: {e}"

    def get_os_name(self, version):
        version_mapping = {
            "14": "macOS Sonoma",
            "13": "macOS Ventura",
            "12": "macOS Monterey",
            "11": "macOS Big Sur",
            "10.15": "macOS Catalina",
            "10.14": "macOS Mojave",
            "10.13": "macOS High Sierra",
            "10.12": "macOS Sierra"
        }
        for key, value in version_mapping.items():
            if version.startswith(key):
                return value
        return "Unknown macOS"

    def export_data(self):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        model_identifier = self.get_model_identifier()
        device_name = self.MODEL_DATABASE.get(model_identifier, "Unknown Model")
        serial_number = self.get_serial_number()
        system_info = self.get_system_information().split('\n')
        battery_info = self.get_battery_information().split('<br>')

        data = (
            f"Exported: {timestamp}\n"
            "------------------------\n\n"
            f"{device_name}\n"
            f"Model Identifier: {model_identifier}\n"
            f"Serial Number: {serial_number}\n"
            f"OS: {system_info[-1]}\n"
            "------------------------\n"
            "Hardware\n"
            "------------------------\n\n"
            f"CPU Type: {system_info[0].split(':')[1].strip()}\n"
            f"CPU Cores: {system_info[1].split(':')[1].strip()}\n\n"
            f"GPU: {system_info[2].split(':')[1].strip()}\n"
            f"VRAM: {system_info[3].split(':')[1].strip()}\n\n"
            f"Memory: {system_info[4].split(':')[1].strip()}\n\n"
            "------------------------\n"
            "Battery\n"
            "------------------------\n\n"
            f"{battery_info[2]}\n"
            "\nGenerated by MacChecker, with love! <3\n"
        )

        options = QtWidgets.QFileDialog.Options()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Data", "macchecker_export.txt", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    file.write(data)
                QtWidgets.QMessageBox.information(self, "MacChecker | Success", "Data exported successfully!")
            except Exception as e:
                QtWidgets.QMessageBox.critical(self, "MacChecker | Error", f"Failed to export data: {e}")

def main():
    app = QtWidgets.QApplication(sys.argv)
    ex = MacInfoApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
