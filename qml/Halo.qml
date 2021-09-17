import QtQuick 2.0

Rectangle {
    property string sfitext // Declare properties here
    property string nameText
    property string clsText
    property string flagText
    property string ownrText
    property string deptText
    property string dateText
    property string hourText
    property string estText
    property string statText

    id: base
    width:30
    height: 100
    // color: "#bdc2e8"
    radius: height/2
    border.width: 2
    anchors.rightMargin: 0
    anchors.bottomMargin: 0
    anchors.leftMargin: 0
    anchors.topMargin: 0
    gradient: Gradient {
        GradientStop {
            position: 0
            color: "#bdc2e8"
        }

        GradientStop {
            position: 0.01
            color: "#bdc2e8"
        }

        GradientStop {
            position: 1
            color: "#e6dee9"
        }
    }

    
    Text{
        id: sfi
        y: 0
        x: 0
        width: parent.height/2
        height: parent.height
        horizontalAlignment: Text.AlignHCenter
        verticalAlignment: Text.AlignVCenter
        // anchors {
        //     verticalCenter: parent.verticalCenter
        // }

        text: sfitext // And use them here

    }
    
    
    Text {
        id: name
        y: parent.height/4
        anchors {
            left: sfi.right
        }
        text: nameText // And use them here
    }
    
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: clsText // And use them here
    }
    
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: flagText // And use them here
    }
    
    
    Text {
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: ownrText // And use them here
    }
    
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: deptText // And use them here
    }
    
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: dateText // And use them here
    }
    
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: hourText // And use them here
    }
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: estText // And use them here
    }
    
    Text{
        anchors {
            top: parent.top
            horizontalCenter: parent.horizontalCenter
        }
        text: statText // And use them here
    }
    
}

