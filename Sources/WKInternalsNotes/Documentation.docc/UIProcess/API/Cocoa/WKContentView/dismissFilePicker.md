# ``WKInternalsNotes/WKContentView/dismissFilePicker()``

テスト用にファイルピッカーを閉じる。

## Objective-C Declaration
```objective-c
- (void)dismissFilePicker;
```

## Discussion
`_fileUploadPanel` に `dismissIfNeededWithReason:Testing` を送る。

## References
- [`WKContentViewInteraction.h#L839`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L839)
- [`WKContentViewInteraction.mm#L7830`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L7830)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
