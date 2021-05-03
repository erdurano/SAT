import QtQuick 2.2
import QtQuick.Window 2.2
import QtQuick.Dialogs.qml 1.0
import QtQuick.Dialogs 1.3
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.2


Item {
    id: window
    width: 1080
    height: 720
    visible: true

    Rectangle {
        id: background
        color: "#ffffff"
        border.width: 0
        anchors.fill: parent


        Rectangle {
            id: topbar
            height: parent.height/10
            opacity: 1
            color: "#8b8989"
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            clip: true
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0
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
                id: completed_test_border
                color: "#ffffff"
                radius: 15
                border.color: "#3c3ed4"
                width: (content_window.width-120)/3
                border.width: 3
                anchors.left: parent.left
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 30
                anchors.topMargin: 30
                anchors.leftMargin: 30


                    Text {
                        id: completed_border_label
                        text: qsTr("Completed")
                        anchors.left: parent.left
                        anchors.top: parent.top
                        font.family: "Effra"
                        font.weight: Font.DemiBold
                        font.pixelSize: 36
                        anchors.leftMargin: height/2
                        anchors.topMargin: -height*5/7
                        z: 1

                        Rectangle {
                            anchors.fill: parent
                            anchors.rightMargin: -3
                            anchors.leftMargin: -3
                            anchors.topMargin: 5
                            color: "#ffffff"
                            z: -1
                        }
                    }
    
                Column {
                    id: column1
                    anchors.fill: completed_test_border


                }
            }

            Rectangle {
                id: active_test_border
                color: "#ffffff"
                width: completed_test_border.width
                radius: 15
                border.color: "#3c3ed4"
                border.width: 3
                anchors.left: completed_test_border.right
                anchors.top: parent.top
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 30
                anchors.leftMargin: 30
                anchors.topMargin: 30

                Text {
                    id: active_border_label
                    text: qsTr("Active")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.family: "Effra"
                    font.weight: Font.DemiBold
                    font.pixelSize: 36
                    anchors.leftMargin: height/2
                    anchors.topMargin: -height*5/7
                    z: 1

                    Rectangle {
                        anchors.fill: parent
                        anchors.rightMargin: -3
                        anchors.leftMargin: -3
                        anchors.topMargin: 5
                        color: "#ffffff"
                        z: -1
                    }
                }

                Column {
                    id: active_column
                    anchors.fill: parent
                    anchors.margins: 5
                    clip: true
                    spacing: 5

                    Repeater {
                        model: itemModel
                        Halo {
                            id: index
                            width: parent.width
                            sfi_label: display["sfi"]

                            // visible : (display["active_stat"] == true) ? true : false


                        

                        }
                    }
                }
            }

            Rectangle {
                id: upcoming_test_border
                x: 1381
                width: completed_test_border.width
                color: "#ffffff"
                radius: 15
                border.color: "#3c3ed4"
                border.width: 3
                anchors.right: parent.right
                anchors.top: parent.top
                anchors.left: active_test_border.right
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 30
                anchors.rightMargin: 30
                anchors.topMargin: 30
                anchors.leftMargin:30

                Text {
                    id: upcoming_border_label
                    text: qsTr("Upcoming")
                    anchors.left: parent.left
                    anchors.top: parent.top
                    font.family: "Effra"
                    font.weight: Font.DemiBold
                    font.pixelSize: 36
                    anchors.leftMargin: height/2
                    anchors.topMargin: -height*5/7
                    z: 1

                    Rectangle {
                        anchors.fill: parent
                        anchors.rightMargin: -3
                        anchors.leftMargin: -3
                        anchors.topMargin: 5
                        color: "#ffffff"
                        z: -1
                    }
                }

                Column {
                    id: column
                    anchors.fill: parent
                }
            }
        }
    }
    
}

