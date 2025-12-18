# ``WKInternalsNotes/_WKInspector/isElementSelectionActive``

要素選択モードが有効かどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL isElementSelectionActive;
```

## Default Value
`false`（`m_elementSelectionActive` の初期値）

## Discussion
`toggleElementSelection` は Start/Stop を送信し、状態は `elementSelectionChanged` で更新される。要素選択が有効になると検査対象ページを前面に出し、解除時はインスペクタを前面に戻す。

## References
- [`_WKInspector.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L50)
- [`_WKInspector.mm#L135`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L135)
- [`WebInspectorUIProxy.h#L204`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L204)
- [`WebInspectorUIProxy.h#L346`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L346)
- [`WebInspectorUIProxy.cpp#L416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L416)
- [`WebInspectorUIProxy.cpp#L760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L760)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
