# ``WKInternalsNotes/WKContentView/selectWordBackwardForTesting()``

テスト用に直前の単語を選択する。

## Objective-C Declaration
```objective-c
- (void)selectWordBackwardForTesting;
```

## Discussion
`_autocorrectionContextNeedsUpdate` を立てたうえで `WebPageProxy` に単語後退選択を依頼する。

## References
- [`WKContentViewInteraction.h#L1029`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1029)
- [`WKContentViewInteraction.mm#L14409`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14409)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
