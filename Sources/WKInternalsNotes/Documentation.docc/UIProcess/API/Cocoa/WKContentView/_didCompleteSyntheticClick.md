# ``WKInternalsNotes/WKContentView/_didCompleteSyntheticClick()``

合成クリック完了時の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_didCompleteSyntheticClick;
```

## Discussion
ポインタ ID を解放し、ログ出力の後に入力ビュー更新のデファリングを解除する。

## References
- [`WKContentViewInteraction.h#L800`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L800)
- [`WKContentViewInteraction.mm#L3974`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3974)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
