import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Dialogs.qml 1.0
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.2


Window {
    id: window
    width: 1920
    height: 1080
    visible: true
    color: "#00000000"
    title: qsTr("SAT Main Window")

    Rectangle {
        id: background
        color: "#ffffff"
        border.width: 0
        anchors.left: parent.left
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
        anchors.rightMargin: 10
        anchors.leftMargin: 10
        anchors.topMargin: 10
        anchors.bottomMargin: 10

        Rectangle {
            id: topbar
            height: 100
            opacity: 1
            color: "#8b8989"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            clip: true
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0

            Rectangle {
                id: load_icon
                x: 1382
                y: 0
                width: topbar.height
                height: topbar.height
                color: "#8b8989"
                anchors.right: parent.right
                anchors.rightMargin: 0
                signal clicked()

                MouseArea {
                    id: load_button
                    hoverEnabled: true
                    anchors.fill: parent
                    onClicked: {fileDialog.open()}
                    onEntered: {
                        load_icon.color = "#858484"
                    }
                    onExited: {
                        load_icon.color = "#8b8989"
                    }
                    Text {
                        text: qsTr("Load file")
                        anchors.fill : parent
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }
        }

        Rectangle {
            id: content_window
            color: "#ffffff"
            radius: 0
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: topbar.bottom
            anchors.bottom: parent.bottom
            anchors.bottomMargin: 0
            anchors.topMargin: 0
            anchors.rightMargin: 0
            anchors.leftMargin: 0

            Rectangle {
                id: active_test_border
                height: 300
                color: "#ffffff"
                radius: 15
                border.color: "#3c3ed4"
                border.width: 3
                anchors.left: parent.left
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.rightMargin: 30
                anchors.leftMargin: 30
                anchors.topMargin: 30

                Text {
                    id: active_border_label
                    width: 156
                    height: 70
                    text: qsTr("Active")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.pixelSize: 36
                    lineHeight: 1.1
                    clip: false
                    anchors.leftMargin: 50
                    anchors.topMargin: -30
                    fontSizeMode: Text.FixedSize
                    minimumPixelSize: 50
                    minimumPointSize: 50
                }
            }

            Rectangle {
                id: compelted_test_border
                width: (content_window.width-90)/2
                color: "#ffffff"
                radius: 15
                border.color: "#3c3ed4"
                border.width: 3
                anchors.left: parent.left
                anchors.top: active_test_border.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 30
                anchors.topMargin: 30
                anchors.leftMargin: 30

                Text {
                    id: completed_border_label
                    width: 190
                    height: 64
                    text: qsTr("Completed")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.pixelSize: 36
                    anchors.leftMargin: 50
                    anchors.topMargin: -30
                }

                Column {
                    id: column1
                    anchors.fill: parent
                }
            }

            Rectangle {
                id: upcoming_test_border
                x: 1381
                width: compelted_test_border.width
                color: "#ffffff"
                radius: 15
                border.color: "#3c3ed4"
                border.width: 3
                anchors.right: parent.right
                anchors.top: active_test_border.bottom
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 30
                anchors.rightMargin: 30
                anchors.topMargin: 30

                Text {
                    id: upcoming_border_label
                    width: 241
                    height: 82
                    text: qsTr("Upcoming")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.pixelSize: 36
                    anchors.leftMargin: 50
                    anchors.topMargin: -30
                }

                Column {
                    id: column
                    anchors.fill: parent
                }
            }
        }
    }
    FileDialog {
        id: fileDialog
        folder:shortcuts.home
        nameFilters: ["Excel SAT form (*.xlsx)"]
        onAccepted: {
        
        }
    }


}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}D{i:4}D{i:10}D{i:13}
}
##^##*/
