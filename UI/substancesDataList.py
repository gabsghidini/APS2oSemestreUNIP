<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>500</height>
   </rect>
  </property>
  <property name="maximumSize">
   <size>
    <width>800</width>
    <height>500</height>
   </size>
  </property>
  <property name="windowTitle">
   <string>Sistema Naval: SS Grupo 10</string>
  </property>
  <property name="styleSheet">
   <string notr="true">background-color: rgb(248, 248, 248)</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="loginTitle">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>20</y>
      <width>361</width>
      <height>31</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Montserrat Medium</family>
      <pointsize>16</pointsize>
      <weight>7</weight>
      <italic>false</italic>
      <bold>false</bold>
     </font>
    </property>
    <property name="styleSheet">
     <string notr="true">font: 57 16pt &quot;Montserrat Medium&quot;;
color: rgb(50, 79, 123);</string>
    </property>
    <property name="text">
     <string>Substâncias:</string>
    </property>
   </widget>
   <widget class="QWidget" name="horizontalLayoutWidget">
    <property name="geometry">
     <rect>
      <x>430</x>
      <y>420</y>
      <width>321</width>
      <height>31</height>
     </rect>
    </property>
    <layout class="QHBoxLayout" name="horizontalLayout">
     <item>
      <widget class="QPushButton" name="backButton">
       <property name="font">
        <font>
         <family>Montserrat SemiBold</family>
         <pointsize>10</pointsize>
         <weight>7</weight>
         <italic>false</italic>
         <bold>false</bold>
        </font>
       </property>
       <property name="styleSheet">
        <string notr="true">font: 63 10pt &quot;Montserrat SemiBold&quot;;
background-color: rgb(134, 166, 223);
color: rgb(248, 248, 248);</string>
       </property>
       <property name="text">
        <string>Voltar</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="comLabel">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>270</y>
      <width>171</width>
      <height>16</height>
     </rect>
    </property>
    <property name="font">
     <font>
      <family>Montserrat Medium</family>
     </font>
    </property>
    <property name="text">
     <string>Comentários / Ocorrências: </string>
    </property>
   </widget>
   <widget class="QLineEdit" name="subsLine">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>300</y>
      <width>721</width>
      <height>101</height>
     </rect>
    </property>
   </widget>
   <widget class="QListWidget" name="listWidget">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>70</y>
      <width>721</width>
      <height>192</height>
     </rect>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>20</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
