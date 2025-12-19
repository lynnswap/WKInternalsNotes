# ``WKInternalsNotes/WKContentView/screenIsBeingCaptured()``

画面キャプチャ中かどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)screenIsBeingCaptured;
```

## Discussion
`UIScreen.isCaptured` を参照する。deprecated API のため `ALLOW_DEPRECATED_DECLARATIONS` で囲まれている。

## References
- [`WKContentView.h#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L90)
- [`WKContentView.mm#L766`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L766)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
