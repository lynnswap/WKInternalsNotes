# ``WKInternalsNotes/WKContentView/_didChangeDragCaretRect(_:currentRect:)``

ドラッグ中のドロップキャレット矩形変更を処理する。

## Objective-C Declaration
```objective-c
- (void)_didChangeDragCaretRect:(CGRect)previousRect currentRect:(CGRect)rect;
```

## Discussion
前後の矩形が空かどうかで挿入・削除を判断し、両方存在する場合はキャレット位置を更新する。

## References
- [`WKContentViewInteraction.h#L900`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L900)
- [`WKContentViewInteraction.mm#L10872`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10872)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
