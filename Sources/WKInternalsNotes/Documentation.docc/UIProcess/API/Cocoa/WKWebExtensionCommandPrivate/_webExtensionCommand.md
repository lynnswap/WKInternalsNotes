# ``WKInternalsNotes/WKWebExtensionCommand/_webExtensionCommand``

内部の `WebKit::WebExtensionCommand` 参照を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebKit::WebExtensionCommand& _webExtensionCommand;
```

## Default Value
初期化後は内部 WebExtensionCommand への参照を保持するため `nil` にならない。

## Discussion
`_webExtensionCommand` を参照して返すだけで、`WKObject` 実装から内部 C++ オブジェクトへアクセスするために使われる。

## References
- [`WKWebExtensionCommandInternal.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommandInternal.h#L42)
- [`WKWebExtensionCommand.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionCommand.mm#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
