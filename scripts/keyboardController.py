#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

import sys
import tty
import termios

class KeyboardController(Node):
    
    def __init__(self):
        super().__init__("keyboard_controller")

        self.publisher = self.create_publisher(
            Twist,
            "/diff_cont/cmd_vel_unstamped",
            10
        )
        self.get_logger().info("Publishing cmd_vel")

    def move_forward(self , x,z):
            msg = Twist()

            msg.linear.x =x
            msg.angular.z=z

            self.get_logger().info(f"Sending: x={x}, z={z}")

            self.publisher.publish(msg)

    def get_key(self):
        fd = sys.stdin.fileno()          # رقم ملف الـ Terminal
        old_settings = termios.tcgetattr(fd)  # حفظ إعدادات الـ Terminal الحالية

        try:
            tty.setraw(fd)               # جعل الـ Terminal يقرأ الحرف مباشرة
            key = sys.stdin.read(1)      # اقرأ حرفًا واحدًا فقط
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)  # إعادة الإعدادات

        return key

    def keyboard_key (self , key):
            if key=="w":
                self.move_forward(1.0 ,0.0)
            elif key =="s":
                self.move_forward(-1.0 ,0.0)
            elif key=="d":
                self.move_forward(0.0 ,-0.5)
            elif key=="a":
                self.move_forward(0.0 ,0.5)
            else:
                self.move_forward(0.0 ,0.0)


def main():
    rclpy.init()
    controller = KeyboardController()

    while rclpy.ok():
        key = controller.get_key()
        controller.keyboard_key(key)
        if key == "q" :
            controller.destroy_node()
            rclpy.shutdown()
            break


if __name__ == '__main__':
    main()