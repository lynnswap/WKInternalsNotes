# ``WKInternalsNotes/WKDeferringGestureRecognizerDelegate/deferringGestureRecognizer(_:didEndTouchesWithEvent:)``

タッチ終了時に遅延ゲートを解除する。

## Objective-C Declaration
```objective-c
- (void)deferringGestureRecognizer:(WKDeferringGestureRecognizer *)deferringGestureRecognizer didEndTouchesWithEvent:(UIEvent *)event;
```

## Discussion
追跡を終了し、状態が `Possible` でなければ終了する。ページが preventable touch を処理中、または `_touchEventGestureRecognizer` が `Possible` の場合は終了し、それ以外は `state` を `Failed` にしてゲートを解除する。

## References
- [`WKDeferringGestureRecognizer.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L40)
- [`WKContentViewInteraction.mm#L10398`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10398)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
