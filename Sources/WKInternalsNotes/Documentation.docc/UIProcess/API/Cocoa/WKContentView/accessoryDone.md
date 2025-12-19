# ``WKInternalsNotes/WKContentView/accessoryDone()``

フォームアクセサリの Done 操作を処理する。

## Objective-C Declaration
```objective-c
- (void)accessoryDone;
```

## Discussion
`_formAccessoryView` を渡して `accessoryViewDone:` を呼び出す。

## References
- [`WKContentViewInteraction.h#L870`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L870)
- [`WKContentViewInteraction.mm#L6219`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6219)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
