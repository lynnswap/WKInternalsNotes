# ``WKInternalsNotes/_WKInspector/togglePageProfiling()``

ページプロファイリングの開始/停止を切り替える。

## Objective-C Declaration
```objective-c
- (void)togglePageProfiling;
```

## Discussion
インスペクタを表示した上で、現在の状態に応じて Start/Stop のメッセージを送信する。状態は `timelineRecordingChanged` で更新される。

## References
- [`_WKInspector.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L57)
- [`_WKInspector.mm#L190`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L190)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
