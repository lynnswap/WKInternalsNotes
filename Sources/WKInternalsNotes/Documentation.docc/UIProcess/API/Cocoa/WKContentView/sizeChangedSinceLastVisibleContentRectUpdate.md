# ``WKInternalsNotes/WKContentView/sizeChangedSinceLastVisibleContentRectUpdate``

可視領域更新以降にサイズ変更があったかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL sizeChangedSinceLastVisibleContentRectUpdate;
```

## Default Value
`didUpdateVisibleRect` 実行後に `NO` へリセットされる。

## Discussion
`VisibleContentRectUpdateInfo` へフラグを渡し、更新完了後に `NO` へ戻す。

## References
- [`WKContentView.h#L64`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L64)
- [`WKContentView.mm#L718`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L718)
- [`WKContentView.mm#L734`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L734)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
