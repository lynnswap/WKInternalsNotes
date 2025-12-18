# ``WKInternalsNotes/_WKInspector/attach()``

インスペクタを検査対象ページにドッキングする。

## Objective-C Declaration
```objective-c
- (void)attach;
```

## Discussion
`WebInspectorUIProxy::attach` を既定の `AttachmentSide::Bottom` で呼び出す。インスペクタページが存在し、ドッキング可能な場合にのみ状態と設定を更新し、SetAttached/Attached* の通知とプラットフォーム処理を行う。

## References
- [`_WKInspector.h#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.h#L55)
- [`_WKInspector.mm#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspector.mm#L180)
- [`WebInspectorUIProxy.h#L191`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.h#L191)
- [`WebInspectorUIProxy.cpp#L318`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp#L318)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
