# ``WKInternalsNotes/WKContentView/reloadContextViewForPresentedListViewController()``

表示中のリストビューコントローラのコンテキストを再読み込みする。

## Objective-C Declaration
```objective-c
- (void)reloadContextViewForPresentedListViewController;
```

## Discussion
`WKTextInputListViewController` が表示中であれば `reloadContextView` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L910`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L910)
- [`WKContentViewInteraction.mm#L8896`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L8896)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
