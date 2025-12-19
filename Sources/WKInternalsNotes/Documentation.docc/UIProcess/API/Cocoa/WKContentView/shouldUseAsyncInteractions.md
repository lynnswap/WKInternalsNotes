# ``WKInternalsNotes/WKContentView/shouldUseAsyncInteractions``

非同期のUIKitインタラクションを使うべきかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL shouldUseAsyncInteractions;
```

## Default Value
`_page->preferences().useAsyncUIKitInteractions()` を返す。

## Discussion
`WebPageProxy` の設定に基づく getter。

## References
- [`WKContentViewInteraction.h#L1014`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1014)
- [`WKContentViewInteraction.mm#L1208`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1208)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
