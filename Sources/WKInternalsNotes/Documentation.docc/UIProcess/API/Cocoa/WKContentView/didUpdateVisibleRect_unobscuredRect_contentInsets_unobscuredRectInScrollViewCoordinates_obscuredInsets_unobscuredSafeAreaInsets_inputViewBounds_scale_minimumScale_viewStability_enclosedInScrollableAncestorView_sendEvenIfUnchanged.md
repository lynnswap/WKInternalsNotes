# ``WKInternalsNotes/WKContentView/didUpdateVisibleRect(_:unobscuredRect:contentInsets:unobscuredRectInScrollViewCoordinates:obscuredInsets:unobscuredSafeAreaInsets:inputViewBounds:scale:minimumScale:viewStability:enclosedInScrollableAncestorView:sendEvenIfUnchanged:)``

可視領域情報を更新して Web プロセスへ通知する。

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
描画領域が無ければ終了。スクロール速度や固定位置レイアウト矩形を計算して `VisibleContentRectUpdateInfo` を構築し、`WebPageProxy` に更新を通知する。レイアウトビューの調整後、内部フラグをリセットし、固定クリッピングビュー更新と安定状態遷移処理を行う。

## References
- [`WKContentView.h#L74`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L74)
- [`WKContentView.mm#L678`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L678)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
