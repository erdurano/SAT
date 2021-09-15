import QtQuick 2.0

Rectangle {
    property string sfitext // Declare properties here

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
        anchors {
            verticalCenter: parent.verticalCenter
            horizontalCenter: parent.horizontalCenter
        }
        text: sfitext // And use them here
    }
    
}

