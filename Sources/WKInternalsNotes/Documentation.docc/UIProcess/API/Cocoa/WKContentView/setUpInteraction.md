# ``WKInternalsNotes/WKContentView/setUpInteraction()``

インタラクション関連の初期化を行う。

## Objective-C Declaration
```objective-c
- (void)setUpInteraction;
```

## Discussion
ページが稼働していれば、コンテナビューやスクロールアニメータ、各種ジェスチャ/インタラクションを作成して登録する。

## References
- [`WKContentViewInteraction.h#L747`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L747)
- [`WKContentViewInteraction.mm#L1290`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1290)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
