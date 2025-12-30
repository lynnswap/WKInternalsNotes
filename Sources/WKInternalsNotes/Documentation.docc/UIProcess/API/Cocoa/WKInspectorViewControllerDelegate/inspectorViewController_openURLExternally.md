# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewController(_:openURLExternally:)``

外部ブラウザで URL を開く要求を通知する。

## Objective-C Declaration
```objective-c
- (void)inspectorViewController:(WKInspectorViewController *)inspectorViewController openURLExternally:(NSURL *)url;
```

## Discussion
`WebInspectorUIProxy` を保持している場合に `openURLExternally(url.absoluteString)` を呼ぶ。

## References
- [`WKInspectorViewController.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L61)
- [`WebInspectorUIProxyMac.mm#L233`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L233)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
