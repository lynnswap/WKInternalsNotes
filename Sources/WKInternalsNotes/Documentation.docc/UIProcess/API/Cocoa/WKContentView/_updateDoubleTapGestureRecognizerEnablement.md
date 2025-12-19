# ``WKInternalsNotes/WKContentView/_updateDoubleTapGestureRecognizerEnablement()``

ダブルタップ系ジェスチャの有効状態を更新する。

## Objective-C Declaration
```objective-c
- (void)_updateDoubleTapGestureRecognizerEnablement;
```

## Discussion
`_doubleTapGestureRecognizer` と `_nonBlockingDoubleTapGestureRecognizer` を `allowsMagnification` と内部フラグに応じて切り替え、ダブルタップ待ち状態をリセットする。

## References
- [`WKContentViewInteraction.h#L1012`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1012)
- [`WKContentViewInteraction.mm#L6210`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L6210)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
