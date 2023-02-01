
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class TrayMenu {
    public void run(){
        TrayIcon trayIcon = null;
        if(SystemTray.isSupported()){
            SystemTray tray = SystemTray.getSystemTray();

            Image img1 = Toolkit.getDefaultToolkit().getImage("img/icon.png");
            Image img2 = Toolkit.getDefaultToolkit().getImage("img/2.png");

            PopupMenu popupMenu = new PopupMenu("Меню");

            MenuItem changeItem = new MenuItem("Изменить");
            trayIcon = new TrayIcon(img1, "Tray Demo", popupMenu);
            TrayIcon finalTrayIcon = trayIcon;
            changeItem.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    finalTrayIcon.setImage(finalTrayIcon.getImage() == img1 ? img2 : img1);
                }
            });
            popupMenu.add(changeItem);

            MenuItem closeItem = new MenuItem("Закрыть");
            closeItem.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    System.exit(0);
                }
            });
            popupMenu.add(closeItem);

            trayIcon.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    JOptionPane.showMessageDialog(null,"Тут пока ничего нет");
                }
            });

            try{
                tray.add(trayIcon);
            }catch (AWTException e) {
                throw new RuntimeException(e);
            }

        }
    }

}
