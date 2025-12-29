# ``WKInternalsNotes/WKMouseInteraction/endPointerLockMouseTracking()``

ポインタロックのマウストラッキングを終了する。

## Objective-C Declaration
```objective-c
- (void)endPointerLockMouseTracking;
```

## Discussion
アクティブでない場合は何もしない。通知監視を停止し、元のマウスムーブハンドラを復元して状態をリセットする。

## References
- [`WKMouseInteraction.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.h#L51)
- [`WKMouseInteraction.mm#L469`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKMouseInteraction.mm#L469)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
