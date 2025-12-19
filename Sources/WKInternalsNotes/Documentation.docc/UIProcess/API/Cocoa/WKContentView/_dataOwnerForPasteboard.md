# ``WKInternalsNotes/WKContentView/_dataOwnerForPasteboard(_:)``

Pasteboard アクセス意図に応じた data owner を返す。

## Objective-C Declaration
```objective-c
- (WebCore::DataOwnerType)_dataOwnerForPasteboard:(WebKit::PasteboardAccessIntent)intent;
```

## Discussion
読み取り/書き込みの意図に応じて `self._dataOwnerForPaste` / `self._dataOwnerForCopy` を選び、`WKWebView` の `effectiveDataOwner` を `WebCore::DataOwnerType` に変換して返す。

## References
- [`WKContentViewInteraction.h#L977`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L977)
- [`WKContentViewInteraction.mm#L10267`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10267)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
