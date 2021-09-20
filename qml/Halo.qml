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

        text: sfitext // And use them here

    }
    
    
    Text {
        id: name
        width: parent.width - parent.height
        height: parent.height/2
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter

        anchors {
        top: parent.top
        horizontalCenter: parent.horizontalCenter
        }
        text: nameText // And use them here
    }
    
    
    Text{
        id: cls
        width: (parent.width - parent.height)/6
        y: parent.height*3/4
        anchors {
            left: sfi.right
        }
        text: "C: " + clsText // And use them here
    }
    
    
    Text{
        id: flag
        width: (parent.width - parent.height)/6
        y: parent.height*3/4
        anchors {
            left: cls.right
            }
        text: "F: " + flagText // And use them here
    }
    
    
    Text {
        width: (parent.width - parent.height)/6
        y: parent.height*3/4
        anchors {
            left: flag.right
        }
        text: "O: " + ownrText // And use them here
    }
    
    
    Text{
        id: dept
        width: (parent.width - parent.height)/2
        height: parent.height/4
        anchors {
            top: parent.verticalCenter
            left: sfi.right
        }
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        text: deptText // And use them here
    }
    
    
    Text{
        id: date
        x: parent.width/2
        y: parent.height/2
        width: (parent.width-parent.height)/2
        height: parent.height/4
        anchors {
            verticalCenter : dept.verticalCenter
        }
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter

        text: dateText // And use them here
    }
    
    
    Text{
        id: startHour
        height: parent.height/4
        width: date.width/2
        anchors {
            left: date.left
            verticalCenter: flag.verticalCenter
        }
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        text: hourText // And use them here
    }
    
    Text{
        height: parent.height/4
        width: date.width/2
        anchors {
            verticalCenter: startHour.verticalCenter
            left: startHour.right
        }
        verticalAlignment: Text.AlignVCenter
        horizontalAlignment: Text.AlignHCenter
        
        text: estText // And use them here
    }
    
    Text{
        x : parent.width - parent.height/2
        anchors {
            verticalCenter: sfi.verticalCenter
        }
        text: statText // And use them here
    }
    
}

