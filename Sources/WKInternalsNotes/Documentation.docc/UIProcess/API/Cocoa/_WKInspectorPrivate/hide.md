# ``WKInternalsNotes/_WKInspector/hide()``

インスペクタ UI を非表示にする。

## Objective-C Declaration
```objective-c
- (void)hide;
```

## Discussion
検査対象ページが存在する場合に `m_isVisible` を `false` にし、プラットフォーム実装で非表示化する。接続自体は維持されるため、非表示でも `isConnected` は `true` のままになり得る。

## References
- [`_WKInspector.h#L53`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L53)
- [`_WKInspector.mm#L150`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L150)
- [`WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
