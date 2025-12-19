# ``WKInternalsNotes/WKContentView/_didPerformDragOperation(_:)``

ドラッグ操作完了後の処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didPerformDragOperation:(BOOL)handled;
```

## Discussion
保留中のペーストボード操作数を減らし、必要なら UIDelegate に完了通知する。座標を算出して状態をクリーンアップし、`dragEnded` を通知する。

## References
- [`WKContentViewInteraction.h#L894`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L894)
- [`WKContentViewInteraction.mm#L10856`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10856)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
