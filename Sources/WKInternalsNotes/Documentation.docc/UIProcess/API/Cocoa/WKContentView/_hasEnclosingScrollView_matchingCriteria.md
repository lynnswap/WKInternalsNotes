# ``WKInternalsNotes/WKContentView/_hasEnclosingScrollView(_:matchingCriteria:)``

指定ビューからスクロールビューの条件一致を判定する。

## Objective-C Declaration
```objective-c
- (BOOL)_hasEnclosingScrollView:(UIView *)firstView matchingCriteria:(Function<BOOL(UIScrollView *)>&&)matchFunction;
```

## Discussion
`firstView` から親ビューを辿り、`UIScrollView` で `matchFunction` が `YES` を返すものがあれば `YES`。`firstView` が無い場合は `webView.scrollView` から開始する。

## References
- [`WKContentViewInteraction.h#L1006`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1006)
- [`WKContentViewInteraction.mm#L3418`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3418)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
