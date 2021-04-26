import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Controls 2.15
import QtQuick.Dialogs 1.3

Window{
    id: main_window
    color: "#ffffff"
    height: 480
    width: 640

    Rectangle{
        anchors.fill: parent
        anchors.margins: 15
        anchors.rightMargin: 15 + scroll.width
        anchors.bottomMargin: 50
        border.color: "black"
        border.width: 1

        ListView{
            id: list_window
            anchors.fill: parent
            anchors.topMargin: 3
            anchors.bottomMargin: 3
            spacing: 3
            focus: true
            clip: true


            model : 30
            delegate: ListItem {
                id: index
            }


            ScrollBar.vertical: ScrollBar {
                id: scroll
                parent: list_window.parent
                anchors.top: parent.top
                anchors.left: parent.right
                anchors.bottom: parent.bottom
                policy: ScrollBar.AlwaysOn
                visible:true
            }  
        }



        Button {
            id: dash_btn
            anchors.left: list_window.left
            anchors.top: list_window.bottom
            anchors.topMargin: 6
            anchors.leftMargin: 3
            text: "Dash It!"
        }

        Button {
            id: imprt_btn
            anchors.verticalCenter: dash_btn.verticalCenter
            anchors.rightMargin: 3
            anchors.right: exprt_btn.left
            text: "Import SAT"
            onClicked: {fileDialog.open()}
        }

        Button {
            id: exprt_btn
            anchors.right: list_window.right
            anchors.verticalCenter: dash_btn.verticalCenter
            anchors.rightMargin: 3
            text: "Export Sat"
        }
    
    }
}   