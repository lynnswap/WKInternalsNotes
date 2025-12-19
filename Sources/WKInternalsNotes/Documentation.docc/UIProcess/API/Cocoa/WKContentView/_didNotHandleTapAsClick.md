# ``WKInternalsNotes/WKContentView/_didNotHandleTapAsClick(_:)``

タップをクリックとして扱わなかった場合の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didNotHandleTapAsClick:(const WebCore::IntPoint&)point;
```

## Discussion
入力ビュー更新の遅延を解除し、ダブルタップ待機中ならスマート拡大を処理して待機を解除する。

## References
- [`WKContentViewInteraction.h#L798`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L798)
- [`WKContentViewInteraction.mm#L3958`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3958)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
