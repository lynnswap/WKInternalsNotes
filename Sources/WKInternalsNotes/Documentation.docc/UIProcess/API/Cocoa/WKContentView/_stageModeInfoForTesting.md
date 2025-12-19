# ``WKInternalsNotes/WKContentView/_stageModeInfoForTesting()``

モデル操作のテスト用ステージ情報を返す。

## Objective-C Declaration
```objective-c
- (NSDictionary *)_stageModeInfoForTesting;
```

## Discussion
`_stageModeSession` が無ければ空の辞書を返し、存在する場合は `awaitingResult` と `hitTestSuccessful` を返す。

## References
- [`WKContentViewInteraction.h#L1047`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1047)
- [`WKContentViewInteraction.mm#L14653`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L14653)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
