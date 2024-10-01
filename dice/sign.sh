~/.cache/briefcase/tools/java17/bin/jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore ~/.android/upload-key-dice.jks "dist/Dice-$1.aab" upload-key -storepass android
