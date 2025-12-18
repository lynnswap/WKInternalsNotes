# ``WKInternalsNotes/_WKInspector/toggleElementSelection()``

要素選択モードの開始/停止を切り替える。

## Objective-C Declaration
```objective-c
- (void)toggleElementSelection;
```

## Discussion
要素選択が有効な場合は Stop を送信し、無効な場合は `connect` してから Start を送信する。状態の更新は `elementSelectionChanged` に委ねられる。

## References
- [`_WKInspector.h#L58`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L58)
- [`_WKInspector.mm#L195`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L195)
- [`WebInspectorUIProxy.cpp#L416`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L416)
- [`WebInspectorUIProxy.cpp#L760`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L760)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
