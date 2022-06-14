import QtQuick
import QtQuick.Window
import QtQuick.Dialogs
import QtQuick.Dialogs
import QtQuick.Layouts
import QtQuick.Controls


Item {
    id: window
    width: 1080
    height: 720
    visible: true

    Fonts{}

    Rectangle {
        id: background
        color: "#ffffff"
        border.width: 0
        anchors.fill: parent


        Rectangle {
            id: topbar
            height: parent.height/10
            opacity: 1
            anchors.left: parent.left
            anchors.right: parent.right
            anchors.top: parent.top
            clip: true
            anchors.rightMargin: 0
            anchors.leftMargin: 0
            anchors.topMargin: 0

            Image{
                fillMode: Image.PreserveAspectFit
                mipmap: true
                source: "../rsrc/img/cemre_logo.png"
                anchors.bottom: parent.bottom
                anchors.bottomMargin: 2
                anchors.left: parent.left
                anchors.leftMargin: 2
                anchors.top: parent.top
                anchors.topMargin: 2
                antialiasing: true
            }

            Text{     
                id : hull_text    
                anchors.verticalCenter: parent.verticalCenter
                anchors.horizontalCenter: parent.horizontalCenter
                text: ScheduleModel.hullNumber
                font.pixelSize: Math.floor(parent.height/2)
                font.weight: Font.Bold
                // color: "#0072ce"
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


                }

                Rectangle {
                    height: 5
                    anchors {
                        top: parent.top
                        left: completed_border_label.left
                        right: completed_border_label.right
                        rightMargin: -3
                        leftMargin: -3
                        topMargin: -1
                    }

                    color: "#ffffff"
                    z: 0

                }
    
                ListView {
                    id: completed_view
                    model: ScheduleModel
                    clip: true
                    anchors.fill: parent
                    anchors.topMargin: 5
                    anchors.bottomMargin: 5
                    anchors.leftMargin:5
                    anchors.rightMargin:5
                    delegate: Halo{
                        visible: model.statusRole == "Passed" || model.statusRole == "Failed" ? true : false
                        height: visible ? passive_view.height/8 : 0
                        anchors.left: parent ? parent.left : undefined
                        anchors.right: parent ? parent.right : undefined
                        sfitext: model.sfiRole
                        nameText: model.nameRole
                        clsText: model.clsRole
                        flagText: model.flagRole
                        ownrText: model.ownrRole
                        deptText: model.deptRole
                        dateText: model.qmlDateRole
                        hourText: model.qmlHourRole
                        estText: model.qmlEstRole
                        statText: model.statusRole
                        respNameText: model.respNameRole
                        isNear: model.isNearRole
                        cemre_font: "Effra"
                    }
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

                }

                Rectangle {
                    height: 5
                    anchors {
                        top: parent.top
                        left: active_border_label.left
                        right: active_border_label.right
                        topMargin: -1
                        rightMargin: -3
                        leftMargin: -3
                    }
                    color: "#ffffff"
                    z: 0
                }
           

                ListView {
                    id: active_view
                    model: ScheduleModel
                    clip: true
                    anchors.fill: parent
                    anchors.topMargin: 5
                    anchors.bottomMargin: 5
                    anchors.leftMargin:5
                    anchors.rightMargin:5
                    delegate: Halo{
                        visible: model.statusRole == "Active" ? true : false
                        height: visible ? passive_view.height/8 : 0
                        anchors.left: parent ? parent.left : undefined
                        anchors.right: parent ? parent.right : undefined
                        sfitext: model.sfiRole
                        nameText: model.nameRole
                        clsText: model.clsRole
                        flagText: model.flagRole
                        ownrText: model.ownrRole
                        deptText: model.deptRole
                        dateText: model.qmlDateRole
                        hourText: model.qmlHourRole
                        estText: model.qmlEstRole
                        statText: model.statusRole
                        respNameText: model.respNameRole
                        isNear: model.isNearRole
                        cemre_font: "Effra"

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

                }

                Rectangle {
                    height: 5
                    anchors {
                        top: parent.top
                        left: upcoming_border_label.left
                        right: upcoming_border_label.right
                        topMargin: -1
                        rightMargin: -3
                        leftMargin: -3
                    }
                    color: "#ffffff"
                    z: 0
                }

                ListView {
                    id: passive_view
                    model: ScheduleModel 
                    clip: true
                    anchors.fill: parent
                    anchors.topMargin: 5
                    anchors.bottomMargin: 5
                    anchors.leftMargin:5
                    anchors.rightMargin:5
                    delegate: Halo{
                        visible: model.statusRole == "Not Started" ? true : false
                        height: visible ? passive_view.height/8 : 0
                        anchors.left: parent ? parent.left : undefined
                        anchors.right: parent ? parent.right : undefined
                        sfitext: model.sfiRole
                        nameText: model.nameRole
                        clsText: model.clsRole
                        flagText: model.flagRole
                        ownrText: model.ownrRole
                        deptText: model.deptRole
                        dateText: model.qmlDateRole
                        hourText: model.qmlHourRole
                        estText: model.qmlEstRole
                        statText: model.statusRole
                        respNameText: model.respNameRole
                        isNear: model.isNearRole
                        cemre_font: "Effra"
                    }
                }
            }
        }
    }
}

