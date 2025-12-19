# ``WKInternalsNotes/WKContentView/_commitPotentialTapFailed()``

潜在タップの確定に失敗した場合の後処理を行う。

## Objective-C Declaration
```objective-c
- (void)_commitPotentialTapFailed;
```

## Discussion
タッチ識別子を解放し、インタラクションをキャンセルして入力ビュー更新の遅延を解除する。

## References
- [`WKContentViewInteraction.h#L797`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L797)
- [`WKContentViewInteraction.mm#L3948`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L3948)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
