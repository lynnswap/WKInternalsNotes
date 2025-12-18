# ``WKInternalsNotes/_WKInspector/isVisible``

インスペクタ UI が表示状態かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isVisible;
```

## Default Value
`false`（初期状態では `m_isVisible` が `false`）

## Discussion
`open` で `m_isVisible` が `true` になり、`hide` と `closeFrontendPageAndWindow` で `false` に戻る。接続状態とは独立しており、接続済みでも非表示の場合は `false` になる。

## References
- [`_WKInspector.h#L47`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L47)
- [`_WKInspector.mm#L120`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L120)
- [`WebInspectorUIProxy.h#L134`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L134)
- [`WebInspectorUIProxy.h#L340`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L340)
- [`WebInspectorUIProxy.cpp#L186`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L186)
- [`WebInspectorUIProxy.cpp#L556`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L556)
- [`WebInspectorUIProxy.cpp#L586`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L586)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
