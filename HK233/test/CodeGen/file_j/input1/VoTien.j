

; VoTien.j

.bytecode 61.0
.source VoTien.java
.class public VoTien
.super java/lang/Object

.method public <init>()V
  .limit stack 1
  .limit locals 1
  .line 6
  0: aload_0
  1: invokespecial java/lang/Object/<init>()V
  4: return
.end method

.method public static main([Ljava/lang/String;)V
  .limit stack 2
  .limit locals 1
  .line 8
  0: getstatic java/lang/System/err Ljava/io/PrintStream;
  3: ldc "VoTien"
  5: invokestatic io/writeString(Ljava/lang/String;)V
  .line 9
  8: return
.end method
                           