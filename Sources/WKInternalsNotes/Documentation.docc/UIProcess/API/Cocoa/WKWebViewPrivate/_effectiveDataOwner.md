# ``WKInternalsNotes/WKWebView/_effectiveDataOwner(_:)``

`_effectiveDataOwner` を実行する。

## Objective-C Declaration
```objective-c
- (_UIDataOwner)_effectiveDataOwner:(_UIDataOwner)clientSuppliedDataOwner;
```

## Discussion
実装は `WKWebView` 側で処理される。

## References
- [`WKWebViewIOS.h#L180`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.h#L180)
- [`WKWebViewIOS.mm#L4043`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/ios/WKWebViewIOS.mm#L4043)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
