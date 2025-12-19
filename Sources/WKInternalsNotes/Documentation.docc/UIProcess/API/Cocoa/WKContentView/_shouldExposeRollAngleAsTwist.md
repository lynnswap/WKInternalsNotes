# ``WKInternalsNotes/WKContentView/_shouldExposeRollAngleAsTwist()``

ロール角を twist として公開するかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)_shouldExposeRollAngleAsTwist;
```

## Discussion
`WebPageProxy` の設定 `exposeRollAngleAsTwistEnabled` を返す。

## References
- [`WKContentView.h#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L144)
- [`WKContentView.mm#L1132`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L1132)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
