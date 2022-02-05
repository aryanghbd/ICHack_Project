package main;

import java.awt.event.ActionListener;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.WindowConstants;
import org.opencv.core.Core;
import org.opencv.videoio.VideoCapture;

public class GUIApp {
  private JFrame frame;
  private JPanel panel;

  public GUIApp() {
    frame = new JFrame("Video Capture");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setExtendedState(JFrame.MAXIMIZED_BOTH);



  }

  private void display() {
    frame.setVisible(true);
  }

  public static void main(String[] args) {
    GUIApp guiApp = new GUIApp();
    guiApp.display();
  }

}
