# ``WKInternalsNotes/WKContentView/accessoryTab(_:)``

フォームアクセサリで前後の要素へ移動する。

## Objective-C Declaration
```objective-c
- (void)accessoryTab:(BOOL)isNext;
```

## Discussion
`isNext` を `TabDirection` に変換し、`accessoryView:tabInDirection:` を呼び出す。

## References
- [`WKContentViewInteraction.h#L872`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L872)
- [`WKContentViewInteraction.mm#L6265`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6265)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
