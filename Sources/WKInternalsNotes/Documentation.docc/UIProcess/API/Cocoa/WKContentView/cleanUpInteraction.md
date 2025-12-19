# ``WKInternalsNotes/WKContentView/cleanUpInteraction()``

インタラクション関連の状態を破棄する。

## Objective-C Declaration
```objective-c
- (void)cleanUpInteraction;
```

## Discussion
アクションシートや入力補助の状態をリセットし、各種ジェスチャ・インタラクションを解除して関連リソースを解放する。

## References
- [`WKContentViewInteraction.h#L748`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L748)
- [`WKContentViewInteraction.mm#L1532`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L1532)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
