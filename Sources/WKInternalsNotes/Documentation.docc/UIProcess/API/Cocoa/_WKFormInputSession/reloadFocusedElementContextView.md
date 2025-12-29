# ``WKInternalsNotes/_WKFormInputSession/reloadFocusedElementContextView()``

フォーカス要素のコンテキストビューを再読み込みする。

## Objective-C Declaration
```objective-c
- (void)reloadFocusedElementContextView WK_API_AVAILABLE(ios(12.0));
```

## Discussion
`WKContentView` の `reloadContextViewForPresentedListViewController` を呼び出す。

## References
- [`WKContentViewInteraction.mm#L903`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L903)
- [`_WKFormInputSession.h#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L48)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
