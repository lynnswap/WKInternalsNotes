# ``WKInternalsNotes/WKWebExtensionAction/_webExtensionAction``

内部の `WebKit::WebExtensionAction` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionAction& _webExtensionAction;
```

## Default Value
初期化後は内部 WebExtensionAction への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionAction` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionActionInternal.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionActionInternal.h#L45)
- [`WKWebExtensionAction.mm#L160`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionAction.mm#L160)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
