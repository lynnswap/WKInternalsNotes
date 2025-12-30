# ``WKInternalsNotes/WKUIScrollEdgeEffect/initWithScrollView(_:scrollEdgeEffect:boxSide:)``

`WKScrollView` と `UIScrollEdgeEffect` を弱参照で保持し、状態を初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithScrollView:(WKScrollView *)scrollView scrollEdgeEffect:(UIScrollEdgeEffect *)effect boxSide:(WebCore::BoxSide)side;
```

## Discussion
`[super init]` の後、`_scrollView` と `_effect`、`_boxSide` を設定し、`_hiddenSources` を空で初期化する。

## References
- [`WKUIScrollEdgeEffect.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.h#L38)
- [`WKUIScrollEdgeEffect.mm#L52`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKUIScrollEdgeEffect.mm#L52)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
