# ``WKInternalsNotes/WKContentView/didUpdateVisibleRect(_:unobscuredRect:contentInsets:unobscuredRectInScrollViewCoordinates:obscuredInsets:unobscuredSafeAreaInsets:inputViewBounds:scale:minimumScale:viewStability:enclosedInScrollableAncestorView:sendEvenIfUnchanged:)``

宣言のみ確認（実装未調査）。

## Objective-C Declaration
```objective-c
- (void)didUpdateVisibleRect:(CGRect)visibleRect
    unobscuredRect:(CGRect)unobscuredRect
    contentInsets:(UIEdgeInsets)contentInsets
    unobscuredRectInScrollViewCoordinates:(CGRect)unobscuredRectInScrollViewCoordinates
    obscuredInsets:(UIEdgeInsets)obscuredInsets
    unobscuredSafeAreaInsets:(UIEdgeInsets)unobscuredSafeAreaInsets
    inputViewBounds:(CGRect)inputViewBounds
    scale:(CGFloat)scale minimumScale:(CGFloat)minimumScale
    viewStability:(OptionSet<WebKit::ViewStabilityFlag>)viewStability
    enclosedInScrollableAncestorView:(BOOL)enclosedInScrollableAncestorView
    sendEvenIfUnchanged:(BOOL)sendEvenIfUnchanged;
```

## Discussion
実装未調査。宣言と対応実装の確認が必要。

## References
- [`WKContentView.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L74)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
